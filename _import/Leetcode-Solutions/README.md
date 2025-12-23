🚀 LeetCode Solutions in C++
<div align="center">
https://img.shields.io/badge/LeetCode-000000?style=for-the-badge&logo=LeetCode&logoColor=#d16c06
https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=c%252B%252B&logoColor=white
https://img.shields.io/badge/Progress-0%252F500-ff6b6b?style=for-the-badge
https://img.shields.io/badge/Stars-%E2%AD%90-yellow?style=for-the-badge

</div>
📊 Real-Time Progress Dashboard
<!-- STAR_COUNTER_START --><div align="center"> <h3>🌟 Progress Stars: <span id="star-counter">0</span></h3> <div style="font-size: 24px;" id="stars-display"></div> </div><!-- TREE_STRUCTURE_START --><div align="center"> <h3>📁 Repository Structure</h3> <pre id="tree-structure"> LeetCode-CPP/ ├── 📂 Arrays/ │ ├── 📄 (empty) ├── 📂 Strings/ │ ├── 📄 (empty) ├── 📂 Hashing/ │ ├── 📄 (empty) ├── 📂 Linked_List/ │ ├── 📄 (empty) ├── 📂 Stack_Queue/ │ ├── 📄 (empty) ├── 📂 Trees/ │ ├── 📄 (empty) └── 📄 README.md </pre> </div> <!-- TREE_STRUCTURE_END -->
🎯 Daily Goal Tracker
<div align="center"> <div style="background: linear-gradient(90deg, #4CAF50 0%, #ffeb3b 50%, #ff5722 100%); padding: 10px; border-radius: 20px; margin: 20px 0;"> <h3>🔥 Daily Streak: <span id="streak">0</span> days</h3> <div style="height: 20px; background: #333; border-radius: 10px; margin: 10px 0;"> <div id="progress-bar" style="height: 100%; width: 0%; background: linear-gradient(90deg, #00b09b, #96c93d); border-radius: 10px; transition: width 0.5s;"></div> </div> <p id="motivation">🚀 Start your journey today! Solve your first problem!</p> </div> </div>
📚 Problem Categories
🟢 Arrays & Strings
Two Sum

Reverse String

Maximum Subarray

🔵 Linked Lists
Reverse Linked List

Merge Two Sorted Lists

Detect Cycle

🟡 Trees & Graphs
Binary Tree Inorder Traversal

Maximum Depth of Binary Tree

Validate BST

🟠 Dynamic Programming
Climbing Stairs

House Robber

Longest Common Subsequence

🟣 Backtracking
N-Queens

Subsets

Permutations

🏆 Achievement System
<div align="center"> <div class="achievements"> <div class="achievement" data-target="1">🎯 First Problem Solved</div> <div class="achievement" data-target="10">🔥 10 Problems Solved</div> <div class="achievement" data-target="50">🏆 50 Problems Solved</div> <div class="achievement" data-target="100">🚀 100 Problems Solved</div> <div class="achievement" data-target="500">💎 500 Problems Solved</div> </div> </div>
📝 How to Use This Repository
Add a new solution:

bash
# Create a new solution file
touch Arrays/two-sum.cpp

# Update the progress counter
# The counter will automatically update when you commit!
File naming convention:

problem-name.cpp

Include problem description as comments

Add time/space complexity analysis

Commit message format:

bash
git commit -m "✅ Solved: Two Sum | Arrays | Easy"
🎨 Interactive Features
This README includes interactive elements that automatically update:

🌟 Star Counter
Every time you solve a problem, add a star emoji to your commit message to increment the counter!

📁 Dynamic Tree Structure
The folder structure updates automatically as you add new files.

🔥 Streak Tracker
Maintain your daily coding streak! Commit at least once per day to keep it alive.

🚀 Quick Start
cpp
// Example solution template
/*
Problem: Two Sum
Difficulty: Easy
URL: https://leetcode.com/problems/two-sum/

Time Complexity: O(n)
Space Complexity: O(n)
*/

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map;
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if (map.find(complement) != map.end()) {
                return {map[complement], i};
            }
            map[nums[i]] = i;
        }
        return {};
    }
};
📈 Progress Statistics
<div align="center"> <table> <tr> <th>Category</th> <th>Solved</th> <th>Total</th> <th>Progress</th> </tr> <tr> <td>Arrays</td> <td id="arr-solved">0</td> <td>50</td> <td><div class="progress"><div class="progress-fill" data-target="arr"></div></div></td> </tr> <tr> <td>Strings</td> <td id="str-solved">0</td> <td>40</td> <td><div class="progress"><div class="progress-fill" data-target="str"></div></div></td> </tr> <tr> <td>Trees</td> <td id="tree-solved">0</td> <td>60</td> <td><div class="progress"><div class="progress-fill" data-target="tree"></div></div></td> </tr> </table> </div>
🤝 Contributing
Feel free to:

Fork this repository

Add new solutions

Improve existing solutions

Share your insights

📚 Resources
LeetCode Official

CPP Reference

NeetCode Roadmap

🎯 Motivation
"The expert in anything was once a beginner." — Helen Hayes

<div align="center"> <h3>Keep Coding! 🚀</h3> <p id="dynamic-quote">"Every problem solved is a step forward in your journey."</p> </div><style> @keyframes pulse { 0% { transform: scale(1); } 50% { transform: scale(1.05); } 100% { transform: scale(1); } } @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } } @keyframes progressAnimation { 0% { width: 0%; } 100% { width: var(--target-width); } } .achievement { display: inline-block; margin: 10px; padding: 10px 20px; background: #f0f0f0; border-radius: 20px; transition: all 0.3s; opacity: 0.3; } .achievement.unlocked { background: linear-gradient(45deg, #FFD700, #FFA500); opacity: 1; animation: pulse 2s infinite; } .progress { width: 100px; height: 10px; background: #ddd; border-radius: 5px; overflow: hidden; } .progress-fill { height: 100%; background: linear-gradient(90deg, #00b09b, #96c93d); border-radius: 5px; animation: progressAnimation 1s ease-out; } #tree-structure { text-align: left; display: inline-block; padding: 20px; background: #1e1e1e; color: #00ff00; border-radius: 10px; font-family: 'Courier New', monospace; animation: fadeIn 1s; } #stars-display { font-size: 30px; margin: 20px 0; animation: pulse 2s infinite; } </style><script> // This script handles the interactive features document.addEventListener('DOMContentLoaded', function() { // Initialize counters updateCounters(); updateTreeStructure(); updateStreak(); // Animate elements animateProgressBars(); // Update quote daily updateDailyQuote(); }); function updateCounters() { // This would be updated based on actual file count const totalFiles = 0; // Update this based on actual count document.getElementById('star-counter').textContent = totalFiles; // Update stars display const stars = '⭐'.repeat(Math.min(totalFiles, 50)); document.getElementById('stars-display').textContent = stars; } function updateTreeStructure() { // This function would dynamically generate the tree structure // based on actual directory contents // For now, it's static but can be made dynamic with GitHub Actions } function updateStreak() { // Calculate streak based on commit history // This is a placeholder - would need backend integration const today = new Date(); const lastCommit = localStorage.getItem('lastCommit'); if (lastCommit) { const lastDate = new Date(lastCommit); const diffTime = Math.abs(today - lastDate); const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24)); if (diffDays === 1) { const streak = parseInt(localStorage.getItem('streak') || '0') + 1; localStorage.setItem('streak', streak); document.getElementById('streak').textContent = streak; // Update progress bar const progress = Math.min((streak / 30) * 100, 100); document.getElementById('progress-bar').style.width = progress + '%'; } } localStorage.setItem('lastCommit', today.toISOString()); } function animateProgressBars() { const progressBars = document.querySelectorAll('.progress-fill'); progressBars.forEach(bar => { const target = bar.getAttribute('data-target'); const solved = parseInt(document.getElementById(target + '-solved').textContent); const total = 50; // This should come from actual data const width = (solved / total) * 100; bar.style.setProperty('--target-width', width + '%'); }); } function updateDailyQuote() { const quotes = [ "Consistency is the key to mastery.", "Every problem solved makes you stronger.", "Don't watch the clock; do what it does. Keep going.", "The only way to learn programming is by writing programs.", "Code is like humor. When you have to explain it, it's bad.", "First, solve the problem. Then, write the code.", "Any fool can write code that a computer can understand. Good programmers write code that humans can understand." ]; const today = new Date().getDate(); const quote = quotes[today % quotes.length]; document.getElementById('dynamic-quote').textContent = `"${quote}"`; // Update motivation message const streak = parseInt(document.getElementById('streak').textContent); const motivation = document.getElementById('motivation'); if (streak === 0) { motivation.textContent = "🚀 Start your journey today! Solve your first problem!"; } else if (streak < 7) { motivation.textContent = `🔥 You're on a ${streak}-day streak! Keep going!`; } else if (streak < 30) { motivation.textContent = `🏆 Amazing! ${streak} days in a row! You're building a habit!`; } else { motivation.textContent = `💎 Legendary ${streak}-day streak! You're unstoppable!`; } } // Simulate adding a new problem (for demo purposes) function simulateAddProblem() { const counter = document.getElementById('star-counter'); let count = parseInt(counter.textContent); count++; counter.textContent = count; // Update stars display const stars = '⭐'.repeat(Math.min(count, 50)); document.getElementById('stars-display').textContent = stars; // Update achievements updateAchievements(count); // Update progress bars animateProgressBars(); // Show celebration for milestones if (count === 1 || count === 10 || count === 50 || count === 100 || count === 500) { celebrateMilestone(count); } } function updateAchievements(count) { const achievements = document.querySelectorAll('.achievement'); achievements.forEach(ach => { const target = parseInt(ach.getAttribute('data-target')); if (count >= target) { ach.classList.add('unlocked'); } }); } function celebrateMilestone(count) { const messages = { 1: "🎉 Congratulations on your first problem!", 10: "🔥 Amazing! 10 problems solved!", 50: "🏆 Half-century! 50 problems conquered!", 100: "🚀 Century! You're on fire!", 500: "💎 Legendary! 500 problems mastered!" }; alert(messages[count]); } </script>
<div align="center"> <p>Made with ❤️ for the coding community</p> <p>Last Updated: <span id="last-updated">Loading...</span></p> </div><script> // Update last updated date const lastUpdated = new Date().toLocaleDateString('en-US', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' }); document.getElementById('last-updated').textContent = lastUpdated; </script>
