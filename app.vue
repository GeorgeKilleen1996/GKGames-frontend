<script setup>
const router = useRouter();
const viewNavbar = ref(true);

watchEffect(() => {
  var path = router.currentRoute.value.path;
  if (path === '/auth/login' || path === '/auth/register') {
    viewNavbar.value = false;
  } else {
    viewNavbar.value = true;
  }
});

</script>
<template>
  <div>
    <NavbarComponent v-if="viewNavbar" />
    <NuxtPage />
  </div>
</template>
