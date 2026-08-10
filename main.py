"""injector_6a48d6 - Structured data handler."""
from dataclasses import dataclass, field, asdict
from typing import List, Optional
import json
@dataclass
class Record:
    id: str
    name: str = "injector_6a48d6"
    tags: List[str] = field(default_factory=list)
    metadata: Optional[dict] = None
    def to_json(self) -> str:
        return json.dumps(asdict(self), indent=2)
@dataclass
class Collection:
    records: List[Record] = field(default_factory=list)
    def add(self, record: Record): self.records.append(record)
    def summary(self) -> dict: return {"count": len(self.records), "ids": [r.id for r in self.records]}
def main():
    col = Collection()
    for i in range(5): col.add(Record(id=f"rec-{i}", tags=["auto"], metadata={"source": "injector_6a48d6"}))
    print(f"Collection: {json.dumps(col.summary(), indent=2)}")
    print(f"Sample: {col.records[0].to_json()}")
if __name__ == "__main__":
    main()
