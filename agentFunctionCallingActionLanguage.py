class AgentFunctionCallingActionLanguage(AgentLanguage):
    def format_actions(self, actions: List[Action]) -> List:
        """Convert actions to function descriptions"""
        return [
            {
                "type": "function",
                "function": {
                    "name": action.name,
                    "description": action.description[:1024],
                    "parameters": action.parameters,
                },
            } 
            for action in actions
        ]

    def construct_prompt(self,
                        actions: List[Action],
                        environment: Environment,
                        goals: List[Goal],
                        memory: Memory) -> Prompt:
        prompt = []
        prompt += self.format_goals(goals)
        prompt += self.format_memory(memory)
        
        tools = self.format_actions(actions)
        
        return Prompt(messages=prompt, tools=tools)

    def parse_response(self, response: str) -> dict:
        """Parse the function call response"""
        try:
            return json.loads(response)
        except Exception as e:
            return {
                "tool": "terminate",
                "args": {"message": response}
            }
