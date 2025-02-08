<script setup>
import Layout from '@components/prelude/Layout.vue';

defineProps({
  workspaces: Array,
});

</script>

<template>
  <Layout>
    {{ workspaces }}
  </Layout>
</template>
