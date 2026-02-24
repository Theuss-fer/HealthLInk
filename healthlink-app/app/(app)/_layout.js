import { Stack, useRouter } from "expo-router";
import { useContext, useEffect } from "react";
import { AuthContext } from "../../src/context/AuthContext";

export default function AppLayout() {
  const { token } = useContext(AuthContext);
  const router = useRouter();

  useEffect(() => {
    if (!token) {
      router.replace("/login");
    }
  }, [token]);

  return <Stack screenOptions={{ headerShown: false }} />;
}
