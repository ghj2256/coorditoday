import React from 'react';

const Location = () => {
  return (
    <div>
      <h4>Using geolocation JavaScript API in React</h4>
      <p>{geolocation()}</p>
    </div>
  );
}

const geolocation = () => {

  let lati, longi;

  navigator.geolocation.getCurrentPosition = (position) => {
    console.log("Latitude is :", position.coords.latitude);
    console.log("Longitude is :", position.coords.longitude);
    lati = position.coords.latitude;
    longi = position.coords.longitude;

    return [lati, longi];
  }

}

export default Location;
