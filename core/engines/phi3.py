import onnxruntime_genai as og

class LLM:
    def __init__(self,api_key) -> None:
        self.api_key = api_key
        self.model_path = "D:\Programming\LLM\phi-3-cpu\cpu_and_mobile\cpu-int4-rtn-block-32-acc-level-4"
        self.model = og.Model(self.model_path)
        print("model loaded")
        self.tokenizer = og.Tokenizer(self.model)
        self.tokenizer_stream = self.tokenizer.create_stream()
        self.chat_template = '<|user|>\n{input} <|end|>\n<|assistant|>'
    
    def generate(self,tk_text_obj,cur_text):
        prompt = f'{self.chat_template.format(input=cur_text)}'
        input_tokens = self.tokenizer.encode(prompt)
        params = og.GeneratorParams(self.model)
        params.input_ids = input_tokens
        generator = og.Generator(self.model, params)
        if cur_text:
            tk_text_obj.insert("end", "\nOutput: ")
        while not generator.is_done():
            generator.compute_logits()
            generator.generate_next_token()
            new_token = generator.get_next_tokens()[0]
            tk_text_obj.insert("end",  self.tokenizer_stream.decode(new_token))
            tk_text_obj.see("end")  # Scroll to the end of the text box
            tk_text_obj.update_idletasks() 
        
