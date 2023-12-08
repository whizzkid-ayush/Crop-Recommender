document.getElementById('recommendationForm').addEventListener('submit', function(event) {
    event.preventDefault();
    let nitrogen = parseFloat(document.getElementById('nitrogen').value);
    // Get values for other input fields in a similar manner
  
    // Perform recommendation logic based on input values
    let recommendedCrop = getRecommendedCrop(nitrogen /*, other parameters */);
  
    // Display recommended crop
    document.getElementById('recommendedCrop').innerText = recommendedCrop;
    document.getElementById('resultSection').classList.remove('hidden');
  });
  
  // Function to determine recommended crop based on input parameters
  function getRecommendedCrop(nitrogen, phosphorus, potassium, temperature) {
    if (nitrogen >= 5) {
      return 'Corn';
    } else if (nitrogen <5) {
      return 'Rice';
    }
      else if (phosphorus >= 5) {
        return 'Carrot';
    }
    else if (phosphorus >= 5) {
        return 'Carrot';
    } else if (phosphorus < 5) {
        return 'Sand';
      } 
    else {
      return 'Other Crop'; // Adjust this else case based on additional conditions
    }
  }