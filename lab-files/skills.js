import React, { useState } from 'react';
import ReactMarkdown from 'react-markdown';

function calculateNumbers(a, b) {
  return a + b;
}

function calculateQuadratic(a, b, c) {
  const d = Math.sqrt(b * b - 4 * a * c);
  const x1 = (-b + d) / (2 * a);
  const x2 = (-b - d) / (2 * a);
  return [x1, x2];
}

// Create a function that calculates the price of a vehicle based on gas mileage, year, and number of miles driven.
function calculatePrice(mpg, year, miles) {
  const age = new Date().getFullYear() - year;
  const price = age * 1000 - miles / mpg;
  return price;
}

function MarkdownEditor() {
    const [markdown, setMarkdown] = useState('type markdown here');

    const handleMarkdownChange = (event) => {
        setMarkdown(event.target.value);
    };

    return (
        <div>
            <textarea value={markdown} onChange={handleMarkdownChange} />
            <ReactMarkdown>{markdown}</ReactMarkdown>
        </div>
    );
}

export default MarkdownEditor;

function reverseSentence(sentence) {
    const reversed = sentence.split(' ').reverse().join(' ');
    return reversed.charAt(0).toUpperCase() + reversed.slice(1);
}

console.log(reverseSentence('hello world')); // World hello
console.log(reverseSentence('the quick brown fox')); // Fox brown quick the
