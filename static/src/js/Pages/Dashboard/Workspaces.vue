<script setup>
import Layout from '@components/prelude/Layout.vue';

defineProps({
  workspaces: Array,
});

</script>

<template>
  <Layout title="workspaces">
    {{ workspaces }}
  </Layout>
</template>
