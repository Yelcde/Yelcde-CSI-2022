package main

import (
	"fmt"
	"net"
	"net/rpc"
	"ifpb/remotelist/pkg"
)

func main() {
	// A inicialização agora pode falhar se o log não puder ser lido/criado
	listService, err := remotelist.NewRemoteListService()
	if err != nil {
		fmt.Println("Server startup error:", err)
		return
	}

	rpcs := rpc.NewServer()
	rpcs.Register(listService) // Registra o serviço
	
	l, e := net.Listen("tcp", "[localhost]:5000")
	if e != nil {
		fmt.Println("listen error:", e)
		return
	}
	defer l.Close()
	
	fmt.Println("RPC Server listening on :5000")
	for {
		conn, err := l.Accept()
		if err == nil {
			go rpcs.ServeConn(conn)
		} else {
			fmt.Println("Accept error:", err)
			break
		}
	}
}