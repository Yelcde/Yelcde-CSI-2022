package remotelist

import (
	"bufio"
	"errors"
	"fmt"
	"os"
	"strconv"
	"strings"
	"sync"
)

// Estrutura que carrega o ID da lista e o valor a ser adicionado
type ListValueArgs struct {
	ListID string 
	Value  int
}

// Estrutura que carrega apenas o ID da lista (usada para operações que não precisam de valor, como remover)
type ListIDArgs struct {
	ListID string
}

// Estrutura para operações que precisam de um índice
type GetArgs struct {
	ListID string 
	Index  int
}

// Contem as listas e o semaforo
// type RemoteListService struct {
// 	mu    sync.Mutex
// 	lists map[string][]int
// }

const logFileName = "remotelist.log"

type RemoteListService struct {
	mu      sync.Mutex
	lists   map[string][]int
	logFile *os.File
}

func NewRemoteListService() (*RemoteListService, error) {
	file, err := os.OpenFile(logFileName, os.O_APPEND|os.O_CREATE|os.O_RDWR, 0666)
	if err != nil {
		return nil, fmt.Errorf("failed to open log file: %w", err)
	}

	service := &RemoteListService{
		lists:   make(map[string][]int),
		logFile: file,
	}

	// Recupera o estado a partir do arquivo de log existente
	if err := service.loadFromLog(); err != nil {
		return nil, fmt.Errorf("failed to load state from log: %w", err)
	}

	fmt.Println("Service initialized and state recovered from log.")
	return service, nil
}

func (rls *RemoteListService) loadFromLog() error {
	// Garante que a leitura comece do início do arquivo
	rls.logFile.Seek(0, 0)
	
	scanner := bufio.NewScanner(rls.logFile)
	for scanner.Scan() {
		line := scanner.Text()
		parts := strings.Split(line, ";")
		if len(parts) < 2 {
			continue // Ignora linhas malformadas
		}

		opType := parts[0]
		listID := parts[1]

		if _, ok := rls.lists[listID]; !ok {
			rls.lists[listID] = make([]int, 0)
		}

		switch opType {
		case "APPEND":
			if len(parts) == 3 {
				value, err := strconv.Atoi(parts[2])
				if err == nil {
					rls.lists[listID] = append(rls.lists[listID], value)
				}
			}
		case "REMOVE":
			if len(rls.lists[listID]) > 0 {
				rls.lists[listID] = rls.lists[listID][:len(rls.lists[listID])-1]
			}
		}
	}
	return scanner.Err()
}

func (rls *RemoteListService) logOperation(format string, args ...interface{}) error {
	logEntry := fmt.Sprintf(format, args...)
	_, err := rls.logFile.WriteString(logEntry + "\n")
	if err != nil {
		return err
	}
	return rls.logFile.Sync()
}

func (rls *RemoteListService) Append(args *ListValueArgs, reply *bool) error {
	rls.mu.Lock()
	defer rls.mu.Unlock()

	if err := rls.logOperation("APPEND;%s;%d", args.ListID, args.Value); err != nil {
		return fmt.Errorf("failed to log append operation: %w", err)
	}

	if _, ok := rls.lists[args.ListID]; !ok {
		rls.lists[args.ListID] = make([]int, 0)
	}

	rls.lists[args.ListID] = append(rls.lists[args.ListID], args.Value)
	fmt.Printf("Appended to %s: %v\n", args.ListID, rls.lists[args.ListID])
	*reply = true
	return nil
}

func (rls *RemoteListService) Remove(args *ListIDArgs, reply *int) error {
	rls.mu.Lock()
	defer rls.mu.Unlock()

	list, ok := rls.lists[args.ListID]
	if !ok {
		return errors.New("list with id " + args.ListID + " not found")
	}

	valueToRemove := list[len(list)-1]
	if err := rls.logOperation("REMOVE;%s;%d", args.ListID, valueToRemove); err != nil {
		return fmt.Errorf("failed to log remove operation: %w", err)
	}

	if len(list) > 0 {
		*reply = list[len(list)-1]
		rls.lists[args.ListID] = list[:len(list)-1]
		fmt.Printf("Removed from %s: New list: %v\n", args.ListID, rls.lists[args.ListID])
	} else {
		return errors.New("empty list for id " + args.ListID)
	}
	return nil
}

// Get retorna o valor da posição i, na lista com identificador list_id. 
func (rls *RemoteListService) Get(args *GetArgs, reply *int) error {
	rls.mu.Lock()
	defer rls.mu.Unlock()

	// Procura a lista pelo ID fornecido.
	list, ok := rls.lists[args.ListID]
	if !ok {
		return fmt.Errorf("list with id '%s' not found", args.ListID)
	}

	// Verifica se o índice está dentro dos limites da lista.
	if args.Index < 0 || args.Index >= len(list) {
		return fmt.Errorf("index %d out of bounds for list with size %d", args.Index, len(list))
	}

	// Se tudo estiver certo, retorna o valor no índice solicitado.
	*reply = list[args.Index]
	
	fmt.Printf("Get from %s[%d]: %d\n", args.ListID, args.Index, *reply)
	return nil
}

// Size obtém a quantidade de elementos armazenados na lista com identificador list_id. 
func (rls *RemoteListService) Size(args *ListIDArgs, reply *int) error {
	rls.mu.Lock()
	defer rls.mu.Unlock()

	// Procura a lista pelo ID fornecido.
	list, ok := rls.lists[args.ListID]
	if !ok {
		return fmt.Errorf("list with id '%s' not found", args.ListID)
	}

	// Retorna o tamanho da lista usando a função len().
	*reply = len(list)
	
	fmt.Printf("Size of %s: %d\n", args.ListID, *reply)
	return nil
}