--Uma empresa de vendas tem um banco de dados com informações sobre os seus produtos. 
--Ela precisa criar um relatório que faça um levantamento diário da quantidade de produtos comprados por dia. 
--Para ajudar a empresa, crie um procedure para agilizar esse processo.


--explicação
-- Essa recebe uma data como parâmetro opcional e retorna a quantidade total de produtos comprados naquele dia. 
--Se a data não for fornecida, ele assumirá o dia atual.

DELIMITER $$

CREATE PROCEDURE RelatorioDiarioCompras(IN data_relatorio DATE)
BEGIN
    SELECT p.data_pedido, SUM(ip.quantidade) AS total_produtos_vendidos
    FROM Pedidos p
    INNER JOIN ItensPedido ip ON p.pedido_id = ip.pedido_id
    WHERE p.data_pedido = data_relatorio
    GROUP BY p.data_pedido;
END$$

DELIMITER ;