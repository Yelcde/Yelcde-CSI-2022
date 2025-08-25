package main

import (
	"log"

	"github.com/Yelcde/microservices/order/config"
	"github.com/Yelcde/microservices/order/internal/adapters/db"
	"github.com/Yelcde/microservices/order/internal/adapters/grpc"
	"github.com/Yelcde/microservices/order/internal/application/core/api"
	//"github.com/Yelcde/microservices/order/internal/adapters/rest"
)

func main() {
	dbAdapter, err := db.NewAdapter(config.GetDataSourceURL())
	if err != nil {
		log.Fatalf("Failed to connect to database. Error: %v", err)
	}
	application := api.NewApplication(dbAdapter)
	grpcAdapter := grpc.NewAdapter(application, config.GetApplicationPort())
	grpcAdapter.Run()
}