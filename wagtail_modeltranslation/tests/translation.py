# -*- coding: utf-8 -*-
from django import VERSION
from django.utils.translation import ugettext_lazy
from wagtail_modeltranslation.tests.models import (
    TestModel, FallbackModel, FallbackModel2, FileFieldsModel, ForeignKeyModel, OtherFieldsModel,
    DescriptorModel, AbstractModelA, AbstractModelB, Slugged, MetaData, Displayable, Page,
    RichText, RichTextPage, MultitableModelA, MultitableModelB, MultitableModelC, ManagerTestModel,
    CustomManagerTestModel, CustomManager2TestModel, GroupFieldsetsModel, NameModel,
    ThirdPartyRegisteredModel, ProxyTestModel, UniqueNullableModel, OneToOneFieldModel,
    RequiredModel, DecoratedModel, TestRootPage, TestSlugPage1, TestSlugPage2, PatchTestPage, PatchTestSnippet,
    FieldPanelPage, ImageChooserPanelPage, FieldRowPanelPage, MultiFieldPanelPage, InlinePanelPage,
    FieldPanelSnippet, ImageChooserPanelSnippet, FieldRowPanelSnippet, MultiFieldPanelSnippet, PageInlineModel,
    BaseInlineModel, StreamFieldPanelPage, StreamFieldPanelSnippet, SnippetInlineModel, InlinePanelSnippet)
from wagtail_modeltranslation.translator import translator, register, TranslationOptions


class TestTranslationOptions(TranslationOptions):
    fields = ('title', 'text', 'url', 'email',)
    empty_values = ''


translator.register(TestModel, TestTranslationOptions)


class UniqueNullableTranslationOptions(TranslationOptions):
    fields = ('title',)


translator.register(UniqueNullableModel, UniqueNullableTranslationOptions)


# ######### Proxy model testing

class ProxyTestTranslationOptions(TranslationOptions):
    fields = ('title', 'text', 'url', 'email',)


translator.register(ProxyTestModel, ProxyTestTranslationOptions)


# ######### Fallback values testing

class FallbackModelTranslationOptions(TranslationOptions):
    fields = ('title', 'text', 'url', 'email', 'description')
    fallback_values = "fallback"


translator.register(FallbackModel, FallbackModelTranslationOptions)


class FallbackModel2TranslationOptions(TranslationOptions):
    fields = ('title', 'text', 'url', 'email',)
    fallback_values = {'text': ugettext_lazy('Sorry, translation is not available.')}
    fallback_undefined = {'title': 'no title'}


translator.register(FallbackModel2, FallbackModel2TranslationOptions)


# ######### File fields testing

class FileFieldsModelTranslationOptions(TranslationOptions):
    fields = ('title', 'file', 'file2', 'image',)


translator.register(FileFieldsModel, FileFieldsModelTranslationOptions)


# ######### Foreign Key / OneToOneField testing

class ForeignKeyModelTranslationOptions(TranslationOptions):
    fields = ('title', 'test', 'optional', 'hidden', 'non',)


translator.register(ForeignKeyModel, ForeignKeyModelTranslationOptions)


class OneToOneFieldModelTranslationOptions(TranslationOptions):
    fields = ('title', 'test', 'optional', 'non',)


translator.register(OneToOneFieldModel, OneToOneFieldModelTranslationOptions)


# ######### Custom fields testing

class OtherFieldsModelTranslationOptions(TranslationOptions):
    fields = ('int', 'boolean', 'nullboolean', 'csi', 'float', 'decimal',
              'ip', 'genericip', 'date', 'datetime', 'time',)


translator.register(OtherFieldsModel, OtherFieldsModelTranslationOptions)


class DescriptorModelTranslationOptions(TranslationOptions):
    fields = ('trans',)


translator.register(DescriptorModel, DescriptorModelTranslationOptions)


# ######### Multitable inheritance testing

class MultitableModelATranslationOptions(TranslationOptions):
    fields = ('titlea',)


translator.register(MultitableModelA, MultitableModelATranslationOptions)


class MultitableModelBTranslationOptions(TranslationOptions):
    fields = ('titleb',)


translator.register(MultitableModelB, MultitableModelBTranslationOptions)


class MultitableModelCTranslationOptions(TranslationOptions):
    fields = ('titlec',)


translator.register(MultitableModelC, MultitableModelCTranslationOptions)


# ######### Abstract inheritance testing

class AbstractModelATranslationOptions(TranslationOptions):
    fields = ('titlea',)


translator.register(AbstractModelA, AbstractModelATranslationOptions)


class AbstractModelBTranslationOptions(TranslationOptions):
    fields = ('titleb',)


translator.register(AbstractModelB, AbstractModelBTranslationOptions)


# ######### Fields inheritance testing

class SluggedTranslationOptions(TranslationOptions):
    fields = ('slug',)


class MetaDataTranslationOptions(TranslationOptions):
    fields = ('keywords',)


class RichTextTranslationOptions(TranslationOptions):
    fields = ('content',)


class PageTranslationOptions(TranslationOptions):
    fields = ('title',)


# BasePage left unregistered intentionally.
translator.register(Slugged, SluggedTranslationOptions)
translator.register(MetaData, MetaDataTranslationOptions)
translator.register(RichText, RichTextTranslationOptions)
translator.register(Displayable)
translator.register(Page, PageTranslationOptions)
translator.register(RichTextPage)


# ######### Manager testing

class ManagerTestModelTranslationOptions(TranslationOptions):
    fields = ('title', 'visits', 'description')


translator.register(ManagerTestModel, ManagerTestModelTranslationOptions)


class CustomManagerTestModelTranslationOptions(TranslationOptions):
    fields = ('title',)


translator.register([CustomManagerTestModel, CustomManager2TestModel],
                    CustomManagerTestModelTranslationOptions)


# ######### TranslationOptions field inheritance testing

class FieldInheritanceATranslationOptions(TranslationOptions):
    fields = ['titlea']


class FieldInheritanceBTranslationOptions(FieldInheritanceATranslationOptions):
    fields = ['titleb']


class FieldInheritanceCTranslationOptions(FieldInheritanceBTranslationOptions):
    fields = ['titlec']


class FieldInheritanceDTranslationOptions(FieldInheritanceBTranslationOptions):
    fields = ('titled',)


class FieldInheritanceETranslationOptions(FieldInheritanceCTranslationOptions,
                                          FieldInheritanceDTranslationOptions):
    fields = ('titlee',)


# ######### Integration testing

class ThirdPartyTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(ThirdPartyRegisteredModel, ThirdPartyTranslationOptions)


# ######### Admin testing

class GroupFieldsetsTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)


translator.register(GroupFieldsetsModel, GroupFieldsetsTranslationOptions)


class NameTranslationOptions(TranslationOptions):
    fields = ('firstname', 'lastname', 'slug2')


translator.register(NameModel, NameTranslationOptions)


# ######### Required fields testing

class RequiredTranslationOptions(TranslationOptions):
    fields = ('non_req', 'req', 'req_reg', 'req_en_reg')
    required_languages = {
        'en': ('req_reg', 'req_en_reg',),
        'default': ('req_reg',),  # for all other languages
    }


translator.register(RequiredModel, RequiredTranslationOptions)


# ######### Decorated registration testing

@register(DecoratedModel)
class DecoratedTranslationOptions(TranslationOptions):
    fields = ('title',)


# ######### 3-rd party with custom manager

if VERSION >= (1, 8):
    from django.contrib.auth.models import Group


    @register(Group)
    class GroupTranslationOptions(TranslationOptions):
        fields = ('name',)


# ######### Wagtail Models

@register(TestRootPage)
class TestRootPagePageTranslationOptions(TranslationOptions):
    fields = ()


@register(TestSlugPage1)
class TestSlugPage1TranslationOptions(TranslationOptions):
    fields = ()


@register(TestSlugPage2)
class TestSlugPage2TranslationOptions(TranslationOptions):
    fields = ()


@register(PatchTestPage)
class PatchTestPageTranslationOptions(TranslationOptions):
    fields = ('description',)


class PatchTestSnippetTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(PatchTestSnippet, PatchTestSnippetTranslationOptions)


# ######### Panel Patching Models

class FieldPanelTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(FieldPanelPage, FieldPanelTranslationOptions)
translator.register(FieldPanelSnippet, FieldPanelTranslationOptions)


class ImageChooserPanelTranslationOptions(TranslationOptions):
    fields = ('image',)


translator.register(ImageChooserPanelPage, ImageChooserPanelTranslationOptions)
translator.register(ImageChooserPanelSnippet, ImageChooserPanelTranslationOptions)


class FieldRowPanelTranslationOptions(TranslationOptions):
    fields = ('other_name',)


translator.register(FieldRowPanelPage, FieldRowPanelTranslationOptions)
translator.register(FieldRowPanelSnippet, FieldRowPanelTranslationOptions)


class StreamFieldPanelTranslationOptions(TranslationOptions):
    fields = ('body',)


translator.register(StreamFieldPanelPage, StreamFieldPanelTranslationOptions)
translator.register(StreamFieldPanelSnippet, StreamFieldPanelTranslationOptions)


class MultiFieldPanelTranslationOptions(TranslationOptions):
    fields = ()


translator.register(MultiFieldPanelPage, MultiFieldPanelTranslationOptions)
translator.register(MultiFieldPanelSnippet, MultiFieldPanelTranslationOptions)


class InlinePanelTranslationOptions(TranslationOptions):
    fields = ('field_name', 'image_chooser', 'fieldrow_name',)


translator.register(BaseInlineModel, InlinePanelTranslationOptions)


class InlinePanelTranslationOptions(TranslationOptions):
    fields = ()


translator.register(PageInlineModel, InlinePanelTranslationOptions)
translator.register(SnippetInlineModel, InlinePanelTranslationOptions)


@register(InlinePanelPage)
class InlinePanelModelTranslationOptions(TranslationOptions):
    fields = ()


translator.register(InlinePanelSnippet, InlinePanelModelTranslationOptions)
