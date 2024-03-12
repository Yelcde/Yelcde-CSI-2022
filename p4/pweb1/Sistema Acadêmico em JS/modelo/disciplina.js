class Disciplina {

    constructor(nome, codigo, alunos = []) {
        this._codigo = codigo;
        this._nome = nome;
        this._alunos = alunos
    }

    set codigo(novoCodigo) {
        this._codigo = novoCodigo;
    }

    set nome(novoNome) {
        this._nome = novoNome;
    }

    set alunos(novoAluno) {
        this.alunos.push(novoAluno);
    }

    get nome() {
        return this._nome;
    }

    get codigo() {
        return this._codigo;
    }

    get alunos() {
        return this._alunos;
    }
}