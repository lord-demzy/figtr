import { cn } from "@/lib/utils";

function Input({ className, type, ...props }: React.ComponentProps<"input">) {
  return (
    <input
      type={type}
      data-slot="input"
      className={cn(
        "file:border-0 file:bg-transparent file:font-medium file:text-sm file:cursor-pointer file:cursor-pointer",
        "flex h-9 w-full min-w-0 rounded-lg border bg-background px-2.5 text-sm text-foreground transition-all",
        "placeholder:text-muted-foreground read-only:bg-muted/50 read-only:focus-within:border-input",
        "focus-visible:border-ring focus-visible:ring-3 focus-visible:ring-ring/50",
        "aria-invalid:border-destructive aria-invalid:ring-3 aria-invalid:ring-destructive/20",
        "disabled:pointer-events-none disabled:cursor-not-allowed disabled:opacity-50",
        "dark:bg-input/30 dark:hover:bg-input/50 dark:focus-within:bg-background dark:focus-within:hover:bg-background",
        "dark:focus-visible:ring-ring/50",
        className
      )}
      {...props}
    />
  );
}

export { Input };
