import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { useContext } from 'react';

import Splash from './screens/Splash';
import Login from './screens/Login';
import Register from './screens/Register';
import Hospitals from './screens/Hospitals';

import { AuthProvider, AuthContext } from './context/AuthContext';

const Stack = createNativeStackNavigator();

function Routes() {
  const { userToken } = useContext(AuthContext);

  return (
    <Stack.Navigator screenOptions={{ headerShown: false }}>
      {userToken ? (
        // 🔒 Rotas protegidas
        <Stack.Screen name="Hospitals" component={Hospitals} />
      ) : (
        // 🌍 Rotas públicas
        <>
          <Stack.Screen name="Splash" component={Splash} />
          <Stack.Screen name="Login" component={Login} />
          <Stack.Screen name="Register" component={Register} />
        </>
      )}
    </Stack.Navigator>
  );
}

export default function App() {
  return (
    <AuthProvider>
      <NavigationContainer>
        <Routes />
      </NavigationContainer>
    </AuthProvider>
  );
}