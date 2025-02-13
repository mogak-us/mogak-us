<script setup lang="ts">
import {
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table'

import { ref, onMounted, defineProps } from 'vue'
import axios from 'axios'

import WorkspaceLayout from '@/layouts/WorkspaceLayout.vue'

const props = defineProps({
  workspace: {
    type: Object,
    required: true,
    validator: (obj) => 'id' in obj && 'name' in obj,
  },
})

const members = ref([])

onMounted(async () => {
  const response = await axios.get(`/api/workspaces/${props.workspace.id}/members/`)
  members.value = response.data
})
</script>

<template>
  <WorkspaceLayout :workspace="workspace">
    <Table>
      <TableCaption>Workspace Members</TableCaption>
      <TableHeader>
        <TableRow>
          <TableHead class="w-[100px]">ID</TableHead>
          <TableHead>Alias Name</TableHead>
        </TableRow>
      </TableHeader>
      <TableBody>
        <TableRow v-for="member in members" :key="member.id">
          <TableCell class="font-medium">{{ member.id }}</TableCell>
          <TableCell>{{ member.alias_name }}</TableCell>
        </TableRow>
      </TableBody>
    </Table>
  </WorkspaceLayout>
</template>
