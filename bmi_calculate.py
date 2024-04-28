# 导包
from decimal import Decimal
# from typing import
import logging
import pandas as pd



logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

class BMICalculator:
    
    UnderWeight="偏瘦"
    NormalWeight="正常"
    OverWeight="过重"
    Obese="肥胖" 
    
    def __init__(self):
        pass
    
    def get_bmi_table(self):
        # bmi | category
        # <18.4 | 偏瘦
        # 18.5-23.9 | 正常
        # 24-27.9 | 过重
        # >28 | 肥胖
        content={
            "BMI": ["<18.4", "18.5~23.9", "24~27.9", ">28"],
            "Category": [self.UnderWeight, self.NormalWeight, self.OverWeight, self.Obese]
        }
        bmi_df=pd.DataFrame(content)
        return bmi_df

    def calculate_bmi(self, weight: float, height: float) -> float:
        """
        Calculate BMI based on weight and height.
        :param weight: Weight in kilograms
        :param height: Height in meters
        :return: BMI value
        """

        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be greater than 0")

        if height >= 2.5:
            raise ValueError(f"Your height input is {height}m, height must be less than 2.5m")

        if weight >= 150:
            raise ValueError(f"Your weight input is {weight}kg, weight must be less than 150kg")

        bmi = weight / (height * height)
        logger.info(f"BMI calculated: {bmi}")
        return round(bmi, 2)

    def get_bmi_category(self, bmi: float) -> str:
        """
        Return the category based on the BMI value.
        :param bmi: BMI value
        :return: Corresponding category
        """
        if bmi < 18.5:
            return self.UnderWeight
        elif bmi < 23.9:
            return self.NormalWeight
        elif bmi < 27.9:
            return self.OverWeight
        else:
            return self.Obese
    # There is no need for exception handling in this function.
    def start(self, weight: float, height: float):
        bmi: float = 0.0
        category: str = ""
        try:
            bmi = self.calculate_bmi(weight, height)
            category = self.get_bmi_category(bmi)
            logger.info(f"Your BMI is {bmi}, and your category is {category}")
        except ValueError as e:
            logger.error(e)
        
        return (bmi, category)

if __name__ == '__main__':
    # 测试
    weight = 70
    height = 1.75
    print()
