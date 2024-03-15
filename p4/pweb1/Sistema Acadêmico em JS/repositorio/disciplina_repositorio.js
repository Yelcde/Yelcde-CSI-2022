class DisciplinaRepositorio {
    
    constructor() {
        this.disciplinas = []
    }

    inserir(disciplina) {
        this.disciplinas.push(disciplina)
    }

    inserirAluno(indexDaDisciplina, aluno) {
        this.disciplinas[indexDaDisciplina].inserirAluno(aluno)
    }

    listar() {
        return this.disciplinas
    }
}