const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('There are infinite portals in front of you, red and blue look most interesting. What do you choose? ', (answer) => {

      console.log(`You entered the ${answer} portal. You are in the ${answer} dimension.`);
    if(answer === 'red' || answer ==='Red') {
      console.log('A red dragon shows up.')
        rl.question('You may burn or freeze the dragon. [burn/freeze] ', (answer) => {
          if(answer === 'burn' || answer === 'Burn') {
            console.log('The dragon is immune. It burns you back. You die.');
            rl.close();
          }
          else if(answer === 'freeze' || answer === 'Freeze') {
            console.log('The dragon is weak to that attack. It is frozen solid! You win!');
            rl.close();
          }

          else {
            console.log('That spell does not work, you die.');
            rl.close();
          }
      })
  }

    else if(answer === 'blue' || answer === 'Blue') {
      console.log('A blue dragon shows up.')
      rl.question('You may burn or freeze the dragon. [burn/freeze] ', (answer) => {
          if(answer === 'burn' || answer === 'Burn') {
            console.log('The dragon is weak to that attack. It is reduced to ashes! You win!');
            rl.close();
          }

          else if(answer === 'freeze' || answer === 'Freeze') {
            console.log('The dragon is immune. It freezes you back. You die.');
            rl.close();
          }

          else {
            console.log('That spell does not work, you die.');
            rl.close();
          }
      })
    }
    else {
      console.log(`You live in the ${answer} dimension for the rest of your life.`)
      rl.close();
    }
});