class DisciplinaControlador {

    constructor() {
        this.servico = new DisciplinaService();
    }

    inserir() {
        const nomeElemento = document.querySelector("#disciplina");
        const codigoElemento = document.querySelector("#codigo");
        const disciplinaInserida = this.servico.inserir(nomeElemento.value, Number(codigoElemento.value));
        const listaDisciplinaElemento = document.querySelector("#listaDisciplina");
        if (disciplinaInserida) {
            this.inserirDisciplinaNoHtml(disciplinaInserida, listaDisciplinaElemento);
        }
    }

    inserirDisciplinaNoHtml(disciplina, elementoDestino) {
        const alunos = disciplina.alunos

        if (alunos.length == 0) {
            alunos.push("Sem Alunos nessa Disciplina")
        }

        const disciplinaElemento = document.createElement("li");
        disciplinaElemento.textContent = `Disciplina: ${disciplina.nome} - Código: ${disciplina.codigo} - Alunos: ${alunos}`;
        elementoDestino.appendChild(disciplinaElemento);
    }

    inserirAlunoEmDisciplina() {
        const codigoElemento = document.querySelector("#codigo");
        const matriculaAluno = document.querySelector("#matriculaAluno");
        this.servico.inserirAluno(codigoElemento, matriculaAluno)
        const listaDisciplinaElemento = document.querySelector("#listaDisciplina");
        const disciplina = this.servico.pesquisarPorCodigo(codigo)
        this.inserirDisciplinaNoHtml(disciplina, listaDisciplinaElemento);
    }
}