package main

import (
	"fmt"
	"net/rpc"
	"ifpb/remotelist/pkg"
)

func main() {
	client, err := rpc.Dial("tcp", "localhost:5000")
	if err != nil {
		fmt.Println("dialing error:", err)
		return
	}
	defer client.Close()

	var successReply bool
	var valueReply int
	var sizeReply int     

	fmt.Println("--- Operações em lista1 ---")
	appendArgs1 := &remotelist.ListValueArgs{ListID: "lista1", Value: 100}
	err = client.Call("RemoteListService.Append", appendArgs1, &successReply)
	if err != nil {
		fmt.Println("Append error:", err)
	} else {
		fmt.Println("Append to lista1 successful:", successReply)
	}

	appendArgs2 := &remotelist.ListValueArgs{ListID: "lista1", Value: 200}
	err = client.Call("RemoteListService.Append", appendArgs2, &successReply)
	if err != nil {
		fmt.Println("Append error:", err)
	} else {
		fmt.Println("Append to lista1 successful:", successReply)
	}

	listIDArgs1 := &remotelist.ListIDArgs{ListID: "lista1"}
	err = client.Call("RemoteListService.Size", listIDArgs1, &sizeReply)
	if err != nil {
		fmt.Println("Size error:", err)
	} else {
		fmt.Println("Size of lista1:", sizeReply)
	}

	getArgs1 := &remotelist.GetArgs{ListID: "lista1", Index: 34}
	err = client.Call("RemoteListService.Get", getArgs1, &valueReply)
	if err != nil {
		fmt.Println("Get error:", err)
	} else {
		fmt.Println("Get from lista1[0]:", valueReply)
	}

	err = client.Call("RemoteListService.Remove", listIDArgs1, &valueReply)
	if err != nil {
		fmt.Println("Remove error:", err)
	} else {
		fmt.Println("Removed from lista1:", valueReply)
	}

	err = client.Call("RemoteListService.Size", listIDArgs1, &sizeReply)
	if err != nil {
		fmt.Println("Size error:", err)
	} else {
		fmt.Println("New size of lista1:", sizeReply)
	}

	fmt.Println("\n--- Operações em lista2 ---")
	appendArgs3 := &remotelist.ListValueArgs{ListID: "lista2", Value: 999}
	err = client.Call("RemoteListService.Append", appendArgs3, &successReply)
	if err != nil {
		fmt.Println("Append error:", err)
	} else {
		fmt.Println("Append to lista2 successful:", successReply)
	}

	listIDArgs2 := &remotelist.ListIDArgs{ListID: "lista2"}
	err = client.Call("RemoteListService.Size", listIDArgs2, &sizeReply)
	if err != nil {
		fmt.Println("Size error:", err)
	} else {
		fmt.Println("Size of lista2:", sizeReply)
	}
}