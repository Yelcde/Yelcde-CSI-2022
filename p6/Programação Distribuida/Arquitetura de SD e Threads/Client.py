import hprose

if __name__ == "__main__":
    client = hprose.HttpClient("http://localhost:80/")  # Ensure the server is running on this URL
    dict_svc = client.useService()

    inserted = dict_svc.update("Johnner", 22)
    print("inseriu Johnner pela 1a vez?", inserted) 

    value = dict_svc.get("Johnner")
    print("valor de Johnner:", value)

    # 3) remove síncrono
    removed = dict_svc.remove("Johnner")
    print("removeu Johnner?", removed)