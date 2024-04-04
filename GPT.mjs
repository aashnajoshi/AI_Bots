import { OpenAI } from 'openai';
import readline from 'readline';
import dotenv from 'dotenv';

dotenv.config();

const openai = new OpenAI({
    apiKey: process.env.GPT_API_KEY,
    dangerouslyAllowBrowser: true
});

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const askQuestion = async () => {
    console.log("Welcome! How can I assist you today?");
    const userResponse = await new Promise(resolve => rl.question("You: ", resolve));

    try {
        const response = await openai.completions.create({
            model: 'gpt-3.5-turbo-instruct',
            prompt: `User: ${userResponse}\nAI:`,
            max_tokens: 150
        });
        console.log(`Bot: ${response.choices[0].text}`);
        const continueResponse = await new Promise(resolve => rl.question("Do you want to explore the bot further? (Y/N): ", resolve));
        if (continueResponse.toLowerCase() === 'n') {
            console.log("Thank you for using our service. Goodbye!");
            rl.close();
            return;
        }
    } catch (error) {
        console.error('An error occurred:', error);
    }
    askQuestion();
};

askQuestion();