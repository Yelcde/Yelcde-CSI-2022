import { Injectable } from '@angular/core';
import {Usuario} from "../model/usuario";
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class UsuarioRestService {

  URL_USUARIOS = 'http://localhost:3000/usuarios';
  constructor(private httpClient: HttpClient) { }

  listar(): Observable<Usuario[]> {
    return this.httpClient.get<Usuario[]>(this.URL_USUARIOS);
  }

  cadastrar_usuario(usuario: Usuario): Observable<Usuario> {
    return this.httpClient.post<Usuario>(this.URL_USUARIOS, usuario);
  }

  deletar_usuario(usuario: Usuario): Observable<Usuario> {
    return this.httpClient.delete<Usuario>(`${this.URL_USUARIOS}/${usuario.id}`);
  }

  editar_usuario(usuario: Usuario): Observable<Usuario> {
    return this.httpClient.put<Usuario>(this.URL_USUARIOS, usuario);
  }
}
