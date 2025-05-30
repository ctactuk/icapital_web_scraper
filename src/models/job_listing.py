from dataclasses import dataclass
from typing import Dict

@dataclass
class JobListing:
    """Data class to represent a job listing"""
    position_title: str
    location: str
    role_description: str

    def to_dict(self) -> Dict[str, str]:
        return {
            "position_title": self.position_title,
            "location": self.location,
            "role_description": self.role_description
        } 