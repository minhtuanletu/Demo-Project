from pydantic import BaseModel

class Result_Model(BaseModel):
    label_image: str
    conf: float
    status: str
    
    def get_values(self):
        return self.label_image, self.conf, self.status
    
    def get_infor(self):
        return {
            "label": self.label_image,
            "conf": self.conf,
            "status": self.status
        }