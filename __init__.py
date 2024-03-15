from ovos_solver_dialogpt import DialoGPTSolver
from ovos_utils import classproperty
from ovos_utils.process_utils import RuntimeRequirements
from ovos_workshop.skills.fallback import FallbackSkill


class DialoGPTSkill(FallbackSkill):

    @classproperty
    def runtime_requirements(self):
        return RuntimeRequirements(internet_before_load=False,
                                   network_before_load=False,
                                   gui_before_load=False,
                                   requires_internet=False,
                                   requires_network=False,
                                   requires_gui=False,
                                   no_internet_fallback=True,
                                   no_network_fallback=True,
                                   no_gui_fallback=True)

    def initialize(self):
        self._chat = DialoGPTSolver(config=self.settings)
        self.register_fallback(self.ask_dialogpt, 88)

    def ask_dialogpt(self, message):
        utterance = message.data['utterance']
        answer = self._chat.get_spoken_answer(utterance, context=message.context)
        if not answer:
            return False
        self.speak(answer)
        return True
