<script setup>
import Layout from '@/layouts/Layout.vue';

defineProps({
  workspaces: Array,
});

</script>

<template>
  <Layout title="workspaces">
    {{ workspaces }}
  </Layout>
</template>
