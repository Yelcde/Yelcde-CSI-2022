class DisciplinaRepositorio {
    
    constructor() {
        this.disciplinas = []
    }

    inserir(disciplina) {
        this.disciplinas.push(disciplina)
    }

    listar() {
        return this.disciplinas
    }
}