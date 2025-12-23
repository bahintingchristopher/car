    const getString = window.location.search;
    console.log(getString); // shows query string

    const myInfo = new URLSearchParams(getString);
    console.log(myInfo);


    console.log(myInfo.get('fullName')); 
    console.log(myInfo.get('phone')); 
    console.log(myInfo.get('email')); 
    console.log(myInfo.get('licenseNumber')); 
    console.log(myInfo.get('licenseExpiry')); 
    console.log(myInfo.get('experience')); 
    console.log(myInfo.get('vehicleModel')); 
    console.log(myInfo.get('testDriveDate')); 
    console.log(myInfo.get('passengers')); 
    console.log(myInfo.get('notes')); 

    const fullName = myInfo.post('fullName'); 
    const phone = myInfo.get('phone'); 
    const email = myInfo.get('email'); 
    const licenseNumber = myInfo.get('licenseNumber'); 
    const licenseExpiry = myInfo.get('licenseExpiry'); 
    const experience = myInfo.get('experience'); 
    const vehicleModel = myInfo.get('vehicleModel'); 
    const testDriveDate = myInfo.get('testDriveDate'); 
    const passengers = myInfo.get('passengers'); 
    const notes = myInfo.get('notes'); 

    document.querySelector('#results').innerHTML = `
    <h2>These are the details from your submission:</h2>
    <p><strong>Full Name:</strong> ${fullName}</p>
    <p><strong>Phone:</strong>  ${phone}</p>
    <p><strong>Email:</strong> ${email}</p>
    <p><strong>Driver's License Number:</strong> ${licenseNumber}</p>
    <p><strong>License Expiry Date:</strong> ${licenseExpiry}</p>
    <p><strong>Driving Experience (years):</strong> ${experience}</p>
    <p><strong>Vehicle Model for Test Drive:</strong> ${vehicleModel}</p>
    <p><strong>Preferred Test Drive Date:</strong> ${testDriveDate}</p>
    <p><strong>Number of Passengers:</strong> ${passengers}</p>
    <p><strong>Additional Notes:</strong> ${notes}</p>
    `;