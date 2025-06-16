class AgentLanguage:
    def construct_prompt(self,
                        actions: List[Action],
                        environment: Environment,
                        goals: List[Goal],
                        memory: Memory) -> Prompt:
        raise NotImplementedError("Subclasses must implement this method")

    def parse_response(self, response: str) -> dict:
        raise NotImplementedError("Subclasses must implement this method")





