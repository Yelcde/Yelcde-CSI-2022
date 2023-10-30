-- 2a parte Aula Triggers (Empregados e departamentos)

-- Exemplo 3

Select * from departamento order by coddepto; 

CREATE OR REPLACE FUNCTION verificaop_Depto() RETURNS TRIGGER AS $$
    BEGIN 
        -- Utiliza a variável TG_OP para descobrir a operação sendo realizada.
        IF (TG_OP = 'DELETE') THEN
            raise notice 'Operação Delete sobre %', TG_TABLE_NAME;
            RETURN OLD;
        ELSIF (TG_OP = 'UPDATE') THEN
            raise notice 'Operação Update sobre %', TG_TABLE_NAME;
            RETURN NEW;
        ELSIF (TG_OP = 'INSERT') THEN
            raise notice 'Operação Insert sobre %', TG_TABLE_NAME;
            RETURN NEW;
        END IF;
        RETURN NULL; 
    END;
    $$ language plpgsql; 
	
-- drop trigger TestaDepto_audit on departamento; 
-- drop trigger TestaDepto_audit2 on departamento;

CREATE TRIGGER TestaDepto_audit
  AFTER INSERT OR UPDATE OR DELETE ON departamento
    FOR EACH ROW EXECUTE PROCEDURE verificaop_Depto();

select * from departamento; 

Insert into departamento values (6,'Compras','Sede');   
update departamento set local = 'Patos' where coddepto = 6; 
delete from departamento where coddepto = 6; 

-- 2a parte do teste 

update departamento 
set local = 'Outro';

drop trigger TestaDepto_audit on departamento;

-- Retire o “for each row”
CREATE TRIGGER TestaDepto_audit2
  AFTER INSERT OR UPDATE OR DELETE ON Departamento
    EXECUTE PROCEDURE verificaop_Depto();

update departamento 
set local = 'teste';

select * from departamento; 