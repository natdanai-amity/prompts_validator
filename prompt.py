from langchain.prompts import PromptTemplate

validator_template = '''You are an intelligent system that will be given two sentences. Your task is to summarize each sentence and determine whether they are similar.
if the sentence ain't similar you have to response "กรุณาติดต่อ call center เพื่อสอบถามข้อมูลเพิ่มเติมค่ะ" , If they are similar Please only response {sentence1}

make decision based ONLY on their factual accuracy. Ignore differences in punctuation and phrasing between the SENTENCE1 and SENTENCE2. It is OK if the sentences contains more information than other sentence, as long as it does not contain any conflicting statements. Begin!

step of working:
-SENTENCE1: "you have to summarize this sentence"
-SENTENCE2: "you have to summarize this sentence"
-DECIDE : similar or not
-REPONSE : answer only {sentence1} if they both similar, if not similar "กรุณาติดต่อ call center เพื่อสอบถามข้อมูลเพิ่มเติมค่ะ" 

Note! do not return result similar word or not similar word

SENTENCE1: {sentence1}
SENTENCE2: {sentence2}
RESPONSE : 


'''

validator_prompt_template = PromptTemplate(template=validator_template, input_variables=['sentence1','sentence2'])