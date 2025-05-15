import hprose

if __name__ == "__main__":
    client = hprose.HttpClient("http://localhost:80/")  # Ensure the server is running on this URL
    dict_svc = client.useService()

    inserted = dict_svc.update("Yelcde", 22)
    print("inseriu Yelcde pela 1a vez?", inserted) 

    value = dict_svc.get("Yelcde")
    print("valor de Yelcde:", value)

    # 3) remove síncrono
    removed = dict_svc.remove("Yelcde")
    print("removeu Yelcde?", removed)