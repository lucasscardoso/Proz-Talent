--Uma loja tem um banco de dados que contém todo o controle de vendas de produtos e de cadastro de clientes.
--Pensando nisso, crie uma função para somar todos os clientes que foram cadastrados na loja durante um dia.

DELIMITER $$

CREATE FUNCTION TotalClientesPorDia(data_cadastro DATE)
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE total_clientes INT;
    
   
    SELECT COUNT(*) INTO total_clientes
    FROM Clientes
    WHERE data_cadastro = data_cadastro;
    
    RETURN total_clientes;
END$$

DELIMITER ;