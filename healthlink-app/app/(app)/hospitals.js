import api from "../services/api";

useEffect(() => {
  async function loadHospitals() {
    try {
      const response = await api.get("/hospitals");
      setHospitals(response.data);
    } catch (error) {
      console.log(error);
    }
  }

  loadHospitals();
}, []);
