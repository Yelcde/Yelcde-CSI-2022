class DisciplinaService {

    constructor() {
        this.repositorio = new DisciplinaRepositorio()
        this.alunoService = new AlunoService()
    }

    inserir(disciplina, codigo) {
        const disciplinaPesquisada = this.pesquisarPorCodigo(codigo);

        if (disciplinaPesquisada.length > 0) {
            throw new Error('Disciplina já cadastrada!');
        }
        
        const disciplinaNova = new Disciplina(disciplina, codigo);
        this.repositorio.inserir(disciplinaNova);
        return disciplinaNova;
    }

    inserirAluno(codigo, matricula) {
        const aluno = this.alunoService.pesquisarPorMatricula(matricula)
        const disciplinas = this.repositorio.listar()
        console.log(disciplinas)
        const index = disciplinas.findIndex(d => d.id === Number(codigo))
        console.log(index)

        if (index === -1) {
            throw new Error("Nenhuma disciplina com esse código!")
        }

        this.repositorio.inserirAluno(index, aluno)
    }

    pesquisarPorCodigo(codigo) {
        return this.repositorio.listar().filter(
            disciplina => disciplina.codigo === codigo);
    }
}