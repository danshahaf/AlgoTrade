import { useState } from 'react'
import axios from "axios";
import logo from './logo.svg';
import './App.css';

function App() {

   // new line start
  const [profileData, setProfileData] = useState(null)

  function getData() {
    axios({
      method: "GET",
      url:"/profile",
    })
    .then((response) => {
      const res =response.data
      setProfileData(({
        profile_name: res.name,
        about_me: res.about}))
    }).catch((error) => {
      if (error.response) {
        console.log(error.response)
        console.log(error.response.status)
        console.log(error.response.headers)
        }
    })}
    //end of new line 

  return (
    <div className="App">
      <header className="App-header">
        <table>
          <tr>
            <th> Leg </th>
            <th> Delta Minimum </th>
            <th> Delta Maximum </th>
            <th> Days Minimum </th>
            <th> Days Maximum </th>
          </tr>
          <tr>
            <td> P1 </td>
            <td> <input type = "number" value = "0.12"/> </td>
            <td> <input type = "number" value = "0.20"/> </td>
            <td> <input type = "number" value = "90"/> </td>
            <td> <input type = "number" value = "130"/> </td>
          </tr>
          <tr>
            <td> P2 </td>
            <td> <input type = "number" value = "0.22"/> </td>
            <td> <input type = "number" value = "0.27"/> </td>
            <td> <input type = "number" value = "40"/> </td>
            <td> <input type = "number" value = "50"/> </td>
          </tr>
          <tr>
            <td> C3 </td>
            <td> <input type = "number" value = "0.22"/> </td>
            <td> <input type = "number" value = "0.27"/> </td>
            <td> <input type = "number" value = "40"/> </td>
            <td> <input type = "number" value = "50"/> </td>
          </tr>
          <tr>
            <td> C4 </td>
            <td> <input type = "number" value = "0.12"/> </td>
            <td> <input type = "number" value = "0.18"/> </td>
            <td> <input type = "number" value = "90"/> </td>
            <td> <input type = "number" value = "130"/> </td>
          </tr>
        </table>

        <button> SUBMIT </button>

        {/* new line start*/}
        <p>To get your profile details: </p><button onClick={getData}>Click me</button>
        {profileData && <div>
              <p>Profile name: {profileData.profile_name}</p>
              <p>About me: {profileData.about_me}</p>
            </div>
        }
         {/* end of new line */}
      </header>
    </div>
  );
}

export default App;