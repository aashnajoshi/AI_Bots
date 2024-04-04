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
    console.log("Choose an option:");
    console.log("1. Answer your query");
    console.log("2. Draw an image based on a prompt");
    console.log("3. Exit");

    const userChoice = await new Promise(resolve => rl.question("Your choice: ", resolve));

    if (userChoice === '1') {
        await chatbot();
    } else if (userChoice === '2') {
        await imageGenerator();
    } else if (userChoice === '3') {
        console.log("Goodbye!");
        rl.close();
    } else {
        console.log("Invalid choice. Please choose again.");
        askQuestion();
    }
};

const chatbot = async () => {
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

const imageGenerator = async () => {
    console.log("Describe the image you want to be generated:");
    const userPrompt = await new Promise(resolve => rl.question("You: ", resolve));

    try {
        const response = await openai.files.create({
            file: userPrompt,
            purpose: "generate an image based on the description provided by the user"
        });
        console.log(`Here's an image link to "${userPrompt}"\n`);
        console.log(response.data.url);
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