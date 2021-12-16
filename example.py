import zootools.client as zcli

cli = zcli.client()

cli.set("teste", b'lucasmoreira')
cli.get("teste")