@dataclass
class Prompt:
    messages: List[Dict] = field(default_factory=list)
    tools: List[Dict] = field(default_factory=list)
    metadata: dict = field(default_factory=dict)  # Fixing mutable default issue



@dataclass(frozen=True)
class Goal:
    priority: int
    name: str
    description: str




class AgentLanguage:
    def construct_prompt(self,
                        actions: List[Action],
                        environment: Environment,
                        goals: List[Goal],
                        memory: Memory) -> Prompt:
        raise NotImplementedError("Subclasses must implement this method")

    def parse_response(self, response: str) -> dict:
        raise NotImplementedError("Subclasses must implement this method")





