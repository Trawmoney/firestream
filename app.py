import { OpenAI } from 'openai'

const fireworks = new OpenAI({
  baseURL: 'https://api.fireworks.ai/inference/v1',
  apiKey: process.env.FIREWORKS_API_KEY
})

// Request the Fireworks API for the response
async function start() {
  const response = await fireworks.completions.create({
    model: accounts/fireworks/models/${model.name},
    stream: true,
    promptOrMessages: buildPrompt(messages),
    max_tokens: 400,
    temperature: 0.5,
    top_p: 1,
    frequency_penalty: 1,
  })

  const result = await response.json();
  const completion = result.choices[0].text
  console.log(completion)
}

start()
