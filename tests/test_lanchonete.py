def test_deve_cancelar_pedido():

    pedido.cancelar()

    assert pedido.esta_cancelado


def test_nao_deve_cancelar_pedido_entregue():

    pedido.entregue = True

    assert pedido.cancelar() is False


def test_deve_adicionar_observacao():

    pedido.adicionar_observacao(
        "Sem cebola"
    )

    assert (
        pedido.observacao
        == "Sem cebola"
    )


def test_nao_deve_aceitar_observacao_vazia():

    assert pedido.adicionar_observacao(
        ""
    ) is False


def test_deve_tornar_pedido_prioritario():

    pedido.tornar_prioritario()

    assert pedido.prioritario


def test_fila_deve_ter_prioritarios_primeiro():

    fila = service.listar_fila_preparo()

    assert fila[0].prioritario


def test_fila_nao_deve_listar_cancelados():

    pedido.cancelar()

    fila = service.listar_fila_preparo()

    assert pedido not in fila