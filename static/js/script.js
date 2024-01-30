// static/js/script.js
function heroTurn(heroName) {
	// Hero's turn logic
	document.getElementById('battle-message').innerText = heroName + "'s turn!";
}

function useSkill(heroName) {
	// Use skill logic
	document.getElementById('battle-message').innerText = heroName + ' uses a skill!';
}

function defend(heroName) {
	// Defend logic
	document.getElementById('battle-message').innerText = heroName + ' defends!';
}
