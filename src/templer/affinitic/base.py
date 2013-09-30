# -*- coding: utf-8 -*-
"""
templer.affinitic

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""


from templer.core.basic_namespace import BasicNamespace
from templer.core.base import get_zopeskel_prefs, wrap_help_paras
from templer.core.create import NoDefault, BadCommand
from templer.core.vars import (
    ValidationException,
    StringVar,
    StringChoiceVar)
from templer.core.base import get_var

from textwrap import TextWrapper


class AffiniticBaseTemplate(BasicNamespace):

    use_cheetah = True

    def __init__(self, *args, **kw):
        super(AffiniticBaseTemplate, self).__init__(*args, **kw)

        # Add new var
        self.vars.insert(3, StringChoiceVar(
            'hoster',
            title='Web hosting service',
            description='If public, choose github. If private, choose bitbucket (github/bitbucket)',
            default='github',
            choices=('github', 'bitbucket'),
        ))

        # Change existing vars
        get_var(self.vars, 'version').default = '0.1'
        get_var(self.vars, 'version').questionable = False

        get_var(self.vars, 'author').default = 'Affinitic'
        get_var(self.vars, 'author').questionable = False

        get_var(self.vars, 'author_email').default = 'info@affinitic.be'
        get_var(self.vars, 'author_email').questionable = False

        get_var(self.vars, 'description').required = True

        get_var(self.vars, 'long_description').questionable = False

        get_var(self.vars, 'keywords').default = 'Affinitic'
        get_var(self.vars, 'keywords').questionable = False

        get_var(self.vars, 'license_name').questionable = False

        get_var(self.vars, 'zip_safe').questionable = False

        get_var(self.vars, 'url').default = 'https://github.com/affinitic/'

        # Remove unwanted vars
        for var in self.vars[:]:
            if var.name == 'expert_mode':
                self.vars.remove(var)

    def check_vars(self, vars, cmd):
        """
        Override of templer.core.base.BaseTemplate.check_vars

        Add the possibility to specify if a variable will
          be questioned in the commande prompt or not
        eg:
            class MyTemplate(AffiniticTemplate):
                vars = copy.deepcopy(BasicNamespace.vars)
                get_var(vars, 'version').questionable = False
        """
        if not hasattr(cmd, '_deleted_once'):
            del vars['package']
            cmd._deleted_once = True

        # if we need to notify users of anything before they start this
        # whole process, we can do it here.
        self.print_zopeskel_message('pre_run_msg')

        # Copied and modified from PasteScript's check_vars--
        # the method there wasn't hookable for the things
        # we need -- question posing, validation, etc.
        #
        # Admittedly, this could be merged into PasteScript,
        # but it was decided it was easier to limit scope of
        # these changes to ZopeSkel, as other projects may
        # use PasteScript in very different ways.

        cmd._deleted_once = 1      # don't re-del package

        textwrapper = TextWrapper(
            initial_indent="|  ",
            subsequent_indent="|  ",
        )

        # now, mostly copied direct from paster
        expect_vars = self.read_vars(cmd)
        if not expect_vars:
            # Assume that variables aren't defined
            return vars
        converted_vars = {}
        errors = []

        config = get_zopeskel_prefs()
        # pastescript allows one to request more than one template (multiple
        # -t options at the command line) so we will get a list of templates
        # from the cmd's options property
        requested_templates = cmd.options.templates
        for var in expect_vars:
            for template in requested_templates:
                if config.has_option(template, var.name):
                    var.default = config.get(template, var.name)
                    break
            else:
                # Not found in template section, now look explicitly
                # in DEFAULT section
                if config.has_option('DEFAULT', var.name):
                    var.default = config.get('DEFAULT', var.name)

        self.override_package_names_defaults(vars, expect_vars)
        unused_vars = vars.copy()

        for var in expect_vars:
            response = self.null_value_marker
            if var.name not in unused_vars:
                if cmd.interactive \
                   and (not hasattr(var, 'questionable')
                        or var.questionable == True):
                    prompt = var.pretty_description()
                    while response is self.null_value_marker:
                        response = cmd.challenge(prompt, var.default,
                                                 var.should_echo)
                        if response == '?':
                            help = var.further_help().strip() % converted_vars
                            print
                            wrap_help_paras(textwrapper, help)
                            print
                            response = self.null_value_marker

                        if hasattr(var, 'required') \
                           and var.required == True \
                           and response.strip() == '':
                            print
                            print "You must answer to this question!"
                            print
                            response = self.null_value_marker

                        if response is not self.null_value_marker:
                            try:
                                response = var.validate(response)
                            except ValidationException, e:
                                print e
                                response = self.null_value_marker
                elif var.default is NoDefault:
                    errors.append('Required variable missing: %s'
                                  % var.full_description())
                else:
                    response = var.validate(var.default)
            else:
                response = var.validate(unused_vars.pop(var.name))

            converted_vars[var.name] = response
            # if a variable has structures associated, we will insert them
            # in the template required_structures property at this time, let's
            # test first to see if we need to do anything.
            if var._is_structural:
                self._set_structure_from_var(var, str(response))

            # filter the vars for mode.
            if var.name == 'expert_mode':
                expert_mode = converted_vars['expert_mode']
                hidden = self._filter_for_modes(expert_mode, expect_vars)
                unused_vars.update(hidden)

            self.process_dependents_vars(vars, var, response, expect_vars)

        if errors:
            raise BadCommand(
                'Errors in variables:\n%s' % '\n'.join(errors))
        converted_vars.update(unused_vars)
        vars.update(converted_vars)

        result = converted_vars

        return result

    def process_dependents_vars(self, vars, changed_var, changed_var_value, expect_vars):
        """
        Process some changes on vars that need to know the value of precedent var
        """
        if changed_var.name == 'hoster':
            if changed_var_value == 'github':
                host = 'github.com'
            elif changed_var_value == 'bitbucket':
                host = 'bitbucket.org'
            url = 'https://%s/affinitic/%s' % (host, vars['project'])
            get_var(expect_vars, 'url').default = url


class AffiniticBaseBuildoutTemplate(AffiniticBaseTemplate):
    category = "Affinitic"
    required_templates = []
    default_required_structures = ['bootstrap', 'gitignore']

    def __init__(self, *args, **kw):
        super(AffiniticBaseBuildoutTemplate, self).__init__(*args, **kw)

        # Add new var
        self.vars.append(StringVar(
            'port',
            title='Zope port',
            description='Specify a port for your zope',
            default='8080',
        ))
