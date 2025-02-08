<script setup>

defineProps({
  workspaces: Array,
});

</script>

<template>
  <Layout>
    {{ workspaces }}
  </Layout>
</template>
