# 🚀 LeetCode Solutions in C++

<div align="center">

![LeetCode](https://img.shields.io/badge/LeetCode-000000?style=for-the-badge&logo=LeetCode&logoColor=#d16c06)
![C++](https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white)
![Progress](https://img.shields.io/badge/Progress-<TOTAL>/500-ff6b6b?style=for-the-badge)
![Stars](https://img.shields.io/badge/Stars-<STARS>-yellow?style=for-the-badge)

</div>

## 📊 Real-Time Progress Dashboard

<div align="center">
  <h3>🌟 Progress Stars: <span id="star-count">0</span></h3>
  <div style="font-size: 24px;" id="stars-display">⭐</div>
</div>

<div align="center">
  <h3>📁 Repository Structure</h3>
  <pre id="folder-structure">
Loading structure...
  </pre>
</div>

## 🎯 Daily Goal Tracker

<div align="center">
  <div style="background: linear-gradient(90deg, #4CAF50 0%, #ffeb3b 50%, #ff5722 100%); padding: 10px; border-radius: 20px; margin: 20px 0;">
    <h3>🔥 Daily Streak: <span id="streak">0</span> days</h3>
    <div style="height: 20px; background: #333; border-radius: 10px; margin: 10px 0;">
      <div id="progress-bar" style="height: 100%; width: 0%; background: linear-gradient(90deg, #00b09b, #96c93d); border-radius: 10px;"></div>
    </div>
    <p id="motivation">🚀 Start your journey today!</p>
  </div>
</div>

## 📚 Problem Categories

### 🟢 Arrays & Strings
- [ ] Two Sum
- [ ] Reverse String
- [ ] Maximum Subarray

### 🔵 Linked Lists
- [ ] Reverse Linked List
- [ ] Merge Two Sorted Lists
- [ ] Detect Cycle

### 🟡 Trees & Graphs
- [ ] Binary Tree Inorder Traversal
- [ ] Maximum Depth of Binary Tree
- [ ] Validate BST

### 🟠 Dynamic Programming
- [ ] Climbing Stairs
- [ ] House Robber
- [ ] Longest Common Subsequence

## 📝 How to Use

1. **Create folders** (any name you want)
2. **Add solution files** (e.g., `two-sum.cpp`)
3. **Run the update script** to auto-count solutions

## 📈 Progress Statistics

<div align="center">
  <table id="progress-table">
    <tr>
      <th>Category</th>
      <th>Solved</th>
      <th>Total</th>
      <th>Progress</th>
    </tr>
    <tr>
      <td>Arrays</td>
      <td id="arr-count">0</td>
      <td>50</td>
      <td><div class="progress"><div id="arr-bar" style="width: 0%"></div></div></td>
    </tr>
    <tr>
      <td>Strings</td>
      <td id="str-count">0</td>
      <td>40</td>
      <td><div class="progress"><div id="str-bar" style="width: 0%"></div></div></td>
    </tr>
  </table>
</div>

<div align="center">
  <p>Made with ❤️ for the coding community</p>
  <p>Last Updated: <span id="last-updated">Loading...</span></p>
</div>

<style>
.progress {
  width: 100px;
  height: 10px;
  background: #ddd;
  border-radius: 5px;
  overflow: hidden;
}

.progress div {
  height: 100%;
  background: linear-gradient(90deg, #00b09b, #96c93d);
  border-radius: 5px;
  transition: width 0.5s;
}

#stars-display {
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0% { transform: scale(1); }
  50% { transform: scale(1.1); }
  100% { transform: scale(1); }
}
</style>

<script>
// Auto-update everything
document.addEventListener('DOMContentLoaded', function() {
  updateAll();
  setInterval(updateAll, 5000); // Update every 5 seconds
});

function updateAll() {
  updateStars();
  updateStreak();
  updateProgress();
  updateStructure();
}

function updateStars() {
  // This counts .cpp files automatically
  fetch('https://api.github.com/repos/YOUR_USERNAME/YOUR_REPO/git/trees/main?recursive=1')
    .then(response => response.json())
    .then(data => {
      const cppFiles = data.tree.filter(item => item.path.endsWith('.cpp'));
      const count = cppFiles.length;
      
      document.getElementById('star-count').textContent = count;
      document.getElementById('stars-display').innerHTML = '⭐'.repeat(Math.min(count, 50));
      
      // Update badges
      document.querySelectorAll('[href*="Progress"]')[0].href = 
        `https://img.shields.io/badge/Progress-${count}%2F500-ff6b6b?style=for-the-badge`;
      document.querySelectorAll('[href*="Stars"]')[0].href = 
        `https://img.shields.io/badge/Stars-${'⭐'.repeat(Math.min(count, 5))}-yellow?style=for-the-badge`;
    });
}

function updateStreak() {
  const today = new Date().toISOString().split('T')[0];
  const lastDate = localStorage.getItem('lastCommit') || today;
  
  if (lastDate === today) {
    const streak = parseInt(localStorage.getItem('streak') || '0') + 1;
    localStorage.setItem('streak', streak);
    document.getElementById('streak').textContent = streak;
    document.getElementById('progress-bar').style.width = Math.min((streak / 30) * 100, 100) + '%';
    
    if (streak === 1) document.getElementById('motivation').textContent = "🔥 First day! Keep going!";
    else if (streak < 7) document.getElementById('motivation').textContent = `🔥 ${streak} day streak!`;
    else document.getElementById('motivation').textContent = `🔥 ${streak} days! You're unstoppable!`;
  }
  
  localStorage.setItem('lastCommit', today);
}

function updateProgress() {
  // Count files per category
  const categories = ['Arrays', 'Strings', 'Trees'];
  
  categories.forEach(cat => {
    const count = Math.floor(Math.random() * 50); // Replace with actual count
    document.getElementById(`${cat.toLowerCase().replace(' ', '-')}-count`).textContent = count;
    document.getElementById(`${cat.toLowerCase().replace(' ', '-')}-bar`).style.width = 
      Math.min((count / 50) * 100, 100) + '%';
  });
}

function updateStructure() {
  fetch('https://api.github.com/repos/YOUR_USERNAME/YOUR_REPO/contents')
    .then(response => response.json())
    .then(data => {
      let structure = 'LeetCode-CPP/\n';
      data.forEach(item => {
        if (item.type === 'dir') {
          structure += `├── 📂 ${item.name}/\n`;
        } else if (item.name === 'README.md') {
          structure += `└── 📄 ${item.name}\n`;
        }
      });
      document.getElementById('folder-structure').textContent = structure;
    });
  
  document.getElementById('last-updated').textContent = new Date().toLocaleString();
}
</script>
