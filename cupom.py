# coding: utf-8

class Loja:
  
  def __init__(self, nome_loja, logradouro, numero, complemento, bairro, 
               municipio, estado, cep, telefone, observacao, cnpj,
               inscricao_estadual):
    self.nome_loja = nome_loja
    self.logradouro = logradouro
    self.numero = numero
    self.complemento = complemento
    self.bairro = bairro
    self.municipio = municipio
    self.estado = estado
    self.cep = cep
    self.telefone = telefone
    self.observacao = observacao
    self.cnpj = cnpj
    self.inscricao_estadual = inscricao_estadual

  def dados_loja(self):

    if not self.nome_loja:
      raise Exception ("O campo nome da loja é obrigatório")

    if not self.logradouro:
      raise Exception ("O campo logradouro do endereço é obrigatório")

    if not self.municipio:
      raise Exception ("O campo município do endereço é obrigatório")

    if not self.estado:
      raise Exception ("O campo estado do endereço é obrigatório")

    if not self.cnpj:
      raise Exception ("O campo CNPJ da loja é obrigatório")

    if not self.inscricao_estadual:
      raise Exception ("O campo inscrição estadual da loja é obrigatório")

    _logradouro = self.logradouro + ", "
    _numero = self.numero and str(self.numero) or "s/n"
    _complemento = self.complemento and " " + self.complemento or ""

    _bairro = self.bairro and self.bairro + " - " or ""
    _municipio = self.municipio + " - "

    _cep = self.cep and ("CEP:" + self.cep) or ""
    _telefone = self.telefone and ("Tel " + self.telefone) or ""
    _telefone = (_telefone and _cep) and (" " + _telefone) or _telefone

    _observacao = self.observacao and self.observacao or ""

    _cnpj = "CNPJ: " + self.cnpj
    _inscricao_estadual = "IE: " + self.inscricao_estadual
    
    return \
f"""{self.nome_loja}
{_logradouro}{_numero}{_complemento}
{_bairro}{_municipio}{self.estado}
{_cep}{_telefone}
{_observacao}
{_cnpj}
{_inscricao_estadual}"""  
