# -*- coding: utf-8 -*-
from five import grok

from datetime import datetime, timedelta

from vindula.themedefault import MessageFactory as _
from Products.CMFCore.utils import getToolByName
from zope.app.component.hooks import getSite

from AccessControl import ClassSecurityInfo
from vindula.themedefault.browser.viewlets import MenuViewlet 

from zope.interface import Interface

from vindula.implantacao.content.interfaces import IImplantacao
from Products.ATContentTypes.content.document import ATDocumentSchema
from Products.ATContentTypes.content.document import ATDocumentBase
from Products.SmartColorWidget.Widget import SmartColorWidget

from zope.interface import implements
from Products.Archetypes.atapi import *
from archetypes.referencebrowserwidget.widget import ReferenceBrowserWidget
from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from vindula.implantacao.config import *

Implantacao_schema =  ATDocumentSchema.copy() + Schema((

                                                     
#Layout  -------------------------------------
    ImageField(
        name='logoCabecalho',
        widget=ImageWidget(
            label=_(u"Logo do cabeçalho"),
            description=_(u""),
            label_msgid='vindula_themedefault_label_logoCabecalho',
            description_msgid='vindula_themedefault_help_logoCabecalho',
            i18n_domain='vindula_implantacao',
        ),
        schemata = 'Layout',
    ),
    
    ImageField(
        name='logoRodape',
        widget=ImageWidget(
            label=_(u"Logo do rodapé"),
            description=_(u""),
            label_msgid='vindula_themedefault_label_logoRodape',
            description_msgid='vindula_themedefault_help_logoRodape',
            i18n_domain='vindula_implantacao',
        ),
        schemata = 'Layout',
    ),
    
    TextField(
        name='rodape',
        default_content_type = 'text/html',
        default_output_type = 'text/x-html-safe',
        searchable = True,
        widget=RichWidget(
            label=_(u"Rodapé"),
            description=_(u""),
            rows=10,
            label_msgid='vindula_themedefault_label_rodape',
            description_msgid='vindula_themedefault_help_rodape',
            i18n_domain='vindula_implantacao',

        ),
        required=False,
        schemata = 'Layout',
    ),
    
    ImageField(
        name='corFundoRodape',
        widget=ImageWidget(
            label=_(u"Cor de fundo do Rodapé"),
            description=_(u""),
            label_msgid='vindula_themedefault_label_corFundoRodape',
            description_msgid='vindula_themedefault_help_corFundoRodape',
            i18n_domain='vindula_implantacao',
        ),
        schemata = 'Layout',
    ),
    
    StringField(
        name = 'corPortal',
        widget=SmartColorWidget(
            label='Cor do portal',
            description="Cor para grande parte do portal.",
            i18n_domain='vindula_implantacao',
        ),
        schemata = 'Layout'
    ),
    
    ImageField(
        name='imagemFundoPortal',
        widget=ImageWidget(
            label=_(u"Imagem de fundo do portal"),
            description=_(u""),
            label_msgid='vindula_themedefault_label_imagemFundoPortal',
            description_msgid='vindula_themedefault_help_imagemFundoPortal',
            i18n_domain='vindula_implantacao',
        ),
        schemata = 'Layout',
    ),
    
    ImageField(
        name='favicon',
        widget=ImageWidget(
            label=_(u"Favicon"),
            description=_(u""),
            label_msgid='vindula_themedefault_label_favicon',
            description_msgid='vindula_themedefault_help_favicon',
            i18n_domain='vindula_implantacao',
        ),
        schemata = 'Layout',
    ),
    
    ImageField(
        name='imagemFundoTelaLogin',
        widget=ImageWidget(
            label=_(u"Imagem de fundo da tela de Login"),
            description=_(u""),
            label_msgid='vindula_themedefault_label_imagemFundoTelaLogin',
            description_msgid='vindula_themedefault_help_imagemFundoTelaLogin',
            i18n_domain='vindula_implantacao',
        ),
        schemata = 'Login',
    ),
    
    StringField(
        name='tipoMenu',
        widget=SelectionWidget(
            label=_(u"tipoMenu"),
            description=_(u""),
            label_msgid='vindula_themedefault_label_type_tipoMenu',
            description_msgid='vindula_themedefault_help_type_tipoMenu',
            i18n_domain='vindula_implantacao',
            format='radio',
        ),
        vocabulary=[('dropdown', 'Drop Down'), ('horizontal', 'Horizontal')],
        default="dropdown",
        schemata = 'Menu',
    ),
    
    BooleanField(
        name='segundoNivelMenu',
        widget=BooleanWidget(
            label=_(u"Segundo Nível de Menu"),
            description=_(u""),
            label_msgid='vindula_themedefault_label_disable_segundoNivelMenu',
            description_msgid='vindula_themedefault_help_disable_segundoNivelMenu',
            i18n_domain='vindula_implantacao',
        ),
        schemata = 'Menu',
    ),
    
    StringField(
        name = 'corFonteMenu',
        widget=SmartColorWidget(
            label='Cor da fonte do Menu',
            description="",
            i18n_domain='vindula_implantacao',
        ),
        schemata = 'Menu'
    ),
    
    StringField(
        name = 'corFundoMenu',
        widget=SmartColorWidget(
            label='Cor do fundo do Menu',
            description="",
            i18n_domain='vindula_implantacao',
        ),
        schemata = 'Menu'
    ),
    
    StringField(
        name = 'corFonteMenuDropDown',
        widget=SmartColorWidget(
            label='Cor da fonte do Menu DropDown',
            description="",
            i18n_domain='vindula_implantacao',
        ),
        schemata = 'Menu'
    ),
    
    StringField(
        name = 'corFundoMenuDropDown',
        widget=SmartColorWidget(
            label='Cor da fundo do Menu DropDown',
            description="",
            i18n_domain='vindula_implantacao',
        ),
        schemata = 'Menu'
    ),

    TextField(
        name='areasEmpresa',
        widget=TextAreaWidget(
            label=_(u"Áreas da Empresa"),
            description=_(u""),
            label_msgid='vindula_controlpanel_label_areasEmpresa',
            description_msgid='vindula_controlpanel_areasEmpresa',
            i18n_domain='vindula_implantacao',
        ),
        schemata = 'Estrutura Organizacional'
    ),
    
    BooleanField(
        name='forum',
        widget=BooleanWidget(
            label=_(u"Fórum"),
            description=_(u""),
            label_msgid='vindula_themedefault_label_disable_forum',
            description_msgid='vindula_themedefault_help_disable_forum',
            i18n_domain='vindula_implantacao',
        ),
        schemata = 'Funcionalidades',
    ),
    
    BooleanField(
        name='enquete',
        widget=BooleanWidget(
            label=_(u"Enquete"),
            description=_(u""),
            label_msgid='vindula_themedefault_label_disable_enquete',
            description_msgid='vindula_themedefault_help_disable_enquete',
            i18n_domain='vindula_implantacao',
        ),
        schemata = 'Funcionalidades',
    ),
    
    BooleanField(
        name='blog',
        widget=BooleanWidget(
            label=_(u"Blog"),
            description=_(u""),
            label_msgid='vindula_themedefault_label_disable_blog',
            description_msgid='vindula_themedefault_help_disable_blog',
            i18n_domain='vindula_implantacao',
        ),
        schemata = 'Funcionalidades',
    ),
    
    BooleanField(
        name='helpDesk',
        widget=BooleanWidget(
            label=_(u"Help Desk"),
            description=_(u""),
            label_msgid='vindula_themedefault_label_disable_helpDesk',
            description_msgid='vindula_themedefault_help_disable_helpDesk',
            i18n_domain='vindula_implantacao',
        ),
        schemata = 'Funcionalidades',
    ),
    
    BooleanField(
        name='chat',
        widget=BooleanWidget(
            label=_(u"Chat"),
            description=_(u""),
            label_msgid='vindula_themedefault_label_disable_chat',
            description_msgid='vindula_themedefault_help_disable_chat',
            i18n_domain='vindula_implantacao',
        ),
        schemata = 'Funcionalidades',
    ),
    
    BooleanField(
        name='classificados',
        widget=BooleanWidget(
            label=_(u"Classificados"),
            description=_(u""),
            label_msgid='vindula_themedefault_label_disable_classificados',
            description_msgid='vindula_themedefault_help_disable_classificados',
            i18n_domain='vindula_implantacao',
        ),
        schemata = 'Funcionalidades',
    ),
    
    BooleanField(
        name='edital',
        widget=BooleanWidget(
            label=_(u"Edital"),
            description=_(u""),
            label_msgid='vindula_themedefault_label_disable_edital',
            description_msgid='vindula_themedefault_help_disable_edital',
            i18n_domain='vindula_implantacao',
        ),
        schemata = 'Funcionalidades',
    ),
    
    BooleanField(
        name='memorando',
        widget=BooleanWidget(
            label=_(u"Memorando"),
            description=_(u""),
            label_msgid='vindula_themedefault_label_disable_memorando',
            description_msgid='vindula_themedefault_help_disable_memorando',
            i18n_domain='vindula_implantacao',
        ),
        schemata = 'Funcionalidades',
    ),
    
    BooleanField(
        name='reservaCorporativa',
        widget=BooleanWidget(
            label=_(u"Reserva Corporativa"),
            description=_(u""),
            label_msgid='vindula_themedefault_label_disable_reservaCorporativa',
            description_msgid='vindula_themedefault_help_disable_reservaCorporativa',
            i18n_domain='vindula_implantacao',
        ),
        schemata = 'Funcionalidades',
    ),
    
    BooleanField(
        name='restaurantes',
        widget=BooleanWidget(
            label=_(u"Restaurantes"),
            description=_(u""),
            label_msgid='vindula_themedefault_label_disable_restaurantes',
            description_msgid='vindula_themedefault_help_disable_restaurantes',
            i18n_domain='vindula_implantacao',
        ),
        schemata = 'Funcionalidades',
    ),
    
    BooleanField(
        name='muralEmpresa',
        widget=BooleanWidget(
            label=_(u"Mural da empresa"),
            description=_(u""),
            label_msgid='vindula_themedefault_label_disable_muralEmpresa',
            description_msgid='vindula_themedefault_help_disable_muralEmpresa',
            i18n_domain='vindula_implantacao',
        ),
        schemata = 'Funcionalidades',
    ),
    
    BooleanField(
        name='visualizacaoHolerites',
        widget=BooleanWidget(
            label=_(u"Visualização de Holerites"),
            description=_(u""),
            label_msgid='vindula_themedefault_label_disable_visualizacaoHolerites',
            description_msgid='vindula_themedefault_help_disable_visualizacaoHolerites',
            i18n_domain='vindula_implantacao',
        ),
        schemata = 'Funcionalidades',
    ),
    
    BooleanField(
        name='memorando',
        widget=BooleanWidget(
            label=_(u"Memorando"),
            description=_(u""),
            label_msgid='vindula_themedefault_label_disable_memorando',
            description_msgid='vindula_themedefault_help_disable_memorando',
            i18n_domain='vindula_implantacao',
        ),
        schemata = 'Funcionalidades',
    ),
    
    BooleanField(
        name='envioDocumentosSetorRH',
        widget=BooleanWidget(
            label=_(u"Envio de Documentos ao setor de RH"),
            description=_(u""),
            label_msgid='vindula_themedefault_label_disable_envioDocumentosSetorRH',
            description_msgid='vindula_themedefault_help_disable_envioDocumentosSetorRH',
            i18n_domain='vindula_implantacao',
        ),
        schemata = 'Funcionalidades',
    ),
    
    BooleanField(
        name='compartilhamentoRedesSociais',
        widget=BooleanWidget(
            label=_(u"Envio de Documentos ao setor de RH"),
            description=_(u""),
            label_msgid='vindula_themedefault_label_disable_compartilhamentoRedesSociais',
            description_msgid='vindula_themedefault_help_disable_compartilhamentoRedesSociais',
            i18n_domain='vindula_implantacao',
        ),
        schemata = 'Funcionalidades',
    ),
    
    StringField(
        name='nomeEmpresa',
        widget=StringWidget(
            label=_(u"Nome da Empresa"),
            description=_(u""),
            label_msgid='vindula_themedefault_label_disable_nomeEmpresa',
            description_msgid='vindula_themedefault_help_disable_nomeEmpresa',
            i18n_domain='vindula_implantacao',
        ),
        schemata = 'Empresa',
    ),
    
    StringField(
        name='nomeFantasia',
        widget=StringWidget(
            label=_(u"Nome da Fantasia"),
            description=_(u""),
            label_msgid='vindula_themedefault_label_disable_nomeFantasia',
            description_msgid='vindula_themedefault_help_disable_nomeFantasia',
            i18n_domain='vindula_implantacao',
        ),
        schemata = 'Empresa',
    ),
    
    StringField(
        name='CNPJ',
        widget=StringWidget(
            label=_(u"CNPJ"),
            description=_(u""),
            label_msgid='vindula_themedefault_label_disable_CNPJ',
            description_msgid='vindula_themedefault_help_disable_CNPJ',
            i18n_domain='vindula_implantacao',
        ),
        schemata = 'Empresa',
    ),
    
    StringField(
        name='telefone',
        widget=StringWidget(
            label=_(u"Telefone"),
            description=_(u""),
            label_msgid='vindula_themedefault_label_disable_telefone',
            description_msgid='vindula_themedefault_help_disable_telefone',
            i18n_domain='vindula_implantacao',
        ),
        schemata = 'Empresa',
    ),
    
    StringField(
        name='endereco',
        widget=StringWidget(
            label=_(u"Endereço"),
            description=_(u""),
            label_msgid='vindula_themedefault_label_disable_endereco',
            description_msgid='vindula_themedefault_help_disable_endereco',
            i18n_domain='vindula_implantacao',
        ),
        schemata = 'Empresa',
    ),
    
    StringField(
        name='cidade',
        widget=StringWidget(
            label=_(u"Cidade"),
            description=_(u""),
            label_msgid='vindula_themedefault_label_disable_cidade',
            description_msgid='vindula_themedefault_help_disable_cidade',
            i18n_domain='vindula_implantacao',
        ),
        schemata = 'Empresa',
    ),
    
    StringField(
        name='estado',
        widget=StringWidget(
            label=_(u"Estado"),
            description=_(u""),
            label_msgid='vindula_themedefault_label_disable_estado',
            description_msgid='vindula_themedefault_help_disable_estado',
            i18n_domain='vindula_implantacao',
        ),
        schemata = 'Empresa',
    ),
    
    StringField(
        name='email',
        widget=StringWidget(
            label=_(u"E-mail"),
            description=_(u""),
            label_msgid='vindula_themedefault_label_disable_email',
            description_msgid='vindula_themedefault_help_disable_email',
            i18n_domain='vindula_implantacao',
        ),
        schemata = 'Empresa',
    ),
    
    StringField(
        name='nomeEmpresa',
        widget=StringWidget(
            label=_(u"Nome da Empresa"),
            description=_(u""),
            label_msgid='vindula_themedefault_label_disable_nomeEmpresa',
            description_msgid='vindula_themedefault_help_disable_nomeEmpresa',
            i18n_domain='vindula_implantacao',
        ),
        schemata = 'Empresa',
    ),
    
    ImageField(
        name='logoEmpresa',
        widget=ImageWidget(
            label=_(u"Logo da empresa"),
            description=_(u""),
            label_msgid='vindula_themedefault_label_logoEmpresa',
            description_msgid='vindula_themedefault_help_logoEmpresa',
            i18n_domain='vindula_implantacao',
        ),
        schemata = 'Empresa',
    ),
    
    StringField(
        name='site',
        widget=StringWidget(
            label=_(u"Site"),
            description=_(u""),
            label_msgid='vindula_themedefault_label_disable_site',
            description_msgid='vindula_themedefault_help_disable_site',
            i18n_domain='vindula_implantacao',
        ),
        validators = ('isURL',),
        schemata = 'Empresa',
        default="http://"
    ),

))
    
finalizeATCTSchema(Implantacao_schema, folderish=False)

invisivel = {'view':'invisible','edit':'invisible',}
Implantacao_schema['description'].widget.visible = invisivel
Implantacao_schema['text'].widget.visible = invisivel

# Dates
L = ['effectiveDate','expirationDate','creation_date','modification_date']   
# Categorization
L += ['subject','relatedItems','location','language']
# Ownership
L += ['creators','contributors','rights']
# Settings
L += ['allowDiscussion','excludeFromNav', 'presentation','tableContents']

for i in L:
    Implantacao_schema[i].widget.visible = invisivel 
    
    
class Implantacao(ATDocumentBase):
    """ HomePage """
    security = ClassSecurityInfo()
    
    implements(IImplantacao)    
    portal_type = 'Implantacao'
    _at_rename_after_creation = True
    schema = Implantacao_schema

registerType(Implantacao, PROJECTNAME)