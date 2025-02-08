<script setup>
import Layout from '@/layouts/Layout.vue';
import WorkspaceItem from '@/components/WorkspaceItem.vue';

defineProps({
  workspaces: Array,
});

</script>

<template>
  <Layout title="Workspaces">
    <div v-for="workspace in workspaces" :key="workspace.id">
      <WorkspaceItem :workspace="workspace" />
    </div>
  </Layout>
</template>
