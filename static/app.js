// ?PREVIOUS NON WORKING ATTEMPT
// UNABLE TO MAKE AN AJAX REQUEST TO WORK , TROUBLE WITH SENDING guess VALUE AND RETRIEVING guess VALUE
// function updateUI(guess) {
//   const output = document.querySelector('#update');
//   output.innerHTML = guess;
// }

// async function sendGuess(event) {
//   event.preventDefault();
//   const $guess = $('#guess').val();
//   const res = await axios({
//     data: { guess: $guess },
//     method: 'POST',
//     url: '/test',
//   });
//   updateUI($guess);
//   console.log(res.data);
//   return res;
// }

// $('#guessForm').on('submit', sendGuess);

// ?async function postData() {

//   let user = {
//     guess:
//   };

//   try {
//     const response = await axios.post("https://reqbin.com/echo/post/json", user);
//     console.log("Request successful!");
//   } catch (error) {
//     if (error.response) {
//       console.log(error.reponse.status);
//     } else {
//       console.log(error.message);
//     }
//   }
// }

// await postData();
